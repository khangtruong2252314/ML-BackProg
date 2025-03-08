from sklearn.naive_bayes import MultinomialNB
# Initialize Multinomial Naive Bayes with Laplace smoothing
nb_classifier = MultinomialNB(alpha=1.0)

# Train the model
nb_classifier.fit(X_train_tfidf, y_train)

# === Genetic Algorithm for Feature Selection ===
class GeneticAlgorithmFeatureSelector:
    def __init__(self, population_size=50, num_generations=20, 
                 mutation_rate=0.1, num_features=2000):
        self.population_size = population_size
        self.num_generations = num_generations
        self.mutation_rate = mutation_rate
        self.num_features = num_features
        self.vectorizer = vectorizer
        self.classifier = MultinomialNB(alpha=1.0)

    # 1. Feature encoding (binary mask: 1=feature selected, 0=feature discarded)
    def initialize_population(self):
        return [np.random.randint(0, 2, self.num_features) 
                for _ in range(self.population_size)]

    # 2. Fitness function (classification accuracy)
    def fitness(self, individual, X_train, X_test, y_train, y_test):
        # Apply feature mask to sparse matrices
        selected_features = np.where(individual == 1)[0]
        if len(selected_features) == 0:  # Prevent empty feature set
            return 0.0
        
        X_train_selected = X_train[:, selected_features]
        X_test_selected = X_test[:, selected_features]
        
        # Train and evaluate
        self.classifier.fit(X_train_selected, y_train)
        y_pred = self.classifier.predict(X_test_selected)
        return accuracy_score(y_test, y_pred)

    # 3. Crossover operator (single-point crossover)
    def crossover(self, parent1, parent2):
        crossover_point = random.randint(1, self.num_features-1)
        child1 = np.concatenate([parent1[:crossover_point], parent2[crossover_point:]])
        child2 = np.concatenate([parent2[:crossover_point], parent1[crossover_point:]])
        return child1, child2

    # 4. Mutation operator
    def mutate(self, individual):
        for i in range(len(individual)):
            if random.random() < self.mutation_rate:
                individual[i] = 1 - individual[i]  # Flip 0 to 1 or 1 to 0
        return individual

    # 5. Selection strategy (tournament selection)
    def tournament_selection(self, population, fitness_scores, tournament_size=3):
        tournament = random.sample(list(zip(population, fitness_scores)), tournament_size)
        return max(tournament, key=lambda x: x[1])[0]

    # Main GA loop
    def evolve(self, X_train, X_test, y_train, y_test):
        population = self.initialize_population()
        best_fitness_history = []

        for generation in range(self.num_generations):
            # Calculate fitness for all individuals
            fitness_scores = [self.fitness(ind, X_train, X_test, y_train, y_test) 
                            for ind in population]
            
            # Track best solution
            best_idx = np.argmax(fitness_scores)
            best_fitness = fitness_scores[best_idx]
            best_individual = population[best_idx]
            best_fitness_history.append(best_fitness)
            
            print(f"Generation {generation+1}/{self.num_generations} - "
                  f"Best Fitness: {best_fitness:.4f}")
            
            # Create new population
            new_population = [best_individual]  # Elitism: keep best solution
            
            while len(new_population) < self.population_size:
                # Selection
                parent1 = self.tournament_selection(population, fitness_scores)
                parent2 = self.tournament_selection(population, fitness_scores)
                
                # Crossover
                child1, child2 = self.crossover(parent1, parent2)
                
                # Mutation
                child1 = self.mutate(child1)
                child2 = self.mutate(child2)
                
                new_population.extend([child1, child2])
            
            population = new_population[:self.population_size]  # Truncate to population size

        # Final evaluation
        best_features = np.where(best_individual == 1)[0]
        print(f"\nBest solution - Number of selected features: {len(best_features)}")
        return best_individual, best_fitness_history

# Run Genetic Algorithm
ga = GeneticAlgorithmFeatureSelector(
    population_size=100,
    num_generations=50,
    mutation_rate=0.1,
    num_features=5000
)

best_features, fitness_history = ga.evolve(
    X_train_tfidf, X_test_tfidf, y_train, y_test
)

# Final model with selected features
final_X_train = X_train_tfidf[:, np.where(best_features == 1)[0]]
final_X_test = X_test_tfidf[:, np.where(best_features == 1)[0]]
final_classifier = MultinomialNB(alpha=1.0)
final_classifier.fit(final_X_train, y_train)