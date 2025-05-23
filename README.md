# ML-BackProg

This project explores various Machine Learning models for sentiment classification on the IMDB dataset. It includes implementations of Decision Trees, Artificial Neural Networks (ANNs) Naive Bayes with Genetic Algorithm and Graphical Models (Bayesian Networks, HMM).

## Dataset :bar_chart:

The project utilizes the [IMDB dataset](https://huggingface.co/datasets/stanfordnlp/imdb) from Hugging Face Datasets. It includes training, testing, and unsupervised splits of movie reviews labeled with sentiment (positive or negative).

## Models :robot:

The following models are implemented and evaluated:

- **Decision Tree:** A classic tree-based model for classification.
- **ANN:** A feedforward neural network using scikit-learn's MLPClassifier.
- **Naive Bayes:** sentiment (S) as dependent on conditionally independent features $\left(F_1, F_2, ..., F_n\right)$ with $P\left(S | F_1, F_2, ..., F_n\right) = P(S) × \prod_i P(F_i | S) / P(F_1, F_2, ..., F_n)$, incorporating sparse feature handling and Laplace smoothing. A Genetic Algorithm optimizes this by encoding features as binary chromosomes, using a fitness function, mutation, crossover, and tournament selection across 50–200 individuals over 50–100 generations
- **Graphical Models:**
    - **Bayesian Network:** A probabilistic graphical model representing conditional dependencies between features and sentiment.
    - **HMM (Hidden Markov Model):** sentiment as a sequence of hidden states (S₁, S₂, ..., Sₜ) emitting observable features (O₁, O₂, ..., Oₜ), with dependencies defined by transition probabilities P(Sₜ | Sₜ₋₁) and emission probabilities P(Oₜ | Sₜ). The model captures temporal dynamics in sentiment, using the Viterbi algorithm for state sequence inference and the Baum-Welch algorithm for training parameters based on observed feature sequences.

## Usage :rocket:

1. **Install Dependencies:** Make sure you have the necessary libraries installed using `pip install -r requirements.txt`.
2. **Run Notebook:** Execute the Jupyter Notebook cells to train and evaluate the models.
3. **Explore Results:** The notebook includes code for generating classification reports, confusion matrices, and other evaluation metrics.


## Results :clipboard:

| Model | Accuracy | Precision | Recall | F1-Score |
|---|---|---|---|---|
| Decision Tree | 0.85 | 0.86 | 0.84 | 0.85 |
| ANN | 0.88 | 0.89 | 0.87 | 0.88 |
| Naive Bayes with Genetic Algorithm | 0.86| 0.86 | 0.86 | 0.86 |
| Bayesian Network | 0.75 | 0.76 | 0.74 | 0.75 |
| HMM | 0.87 | 0.88 | 0.86 | 0.87 |


## Team Members and Their Contributions :busts_in_silhouette:

| Team Member | Contribution | Distribution |
|---|---|---|
| Truong Minh Khang | Decision tree, ANN | 100% |
| Nguyen Minh Khoi | Naive Bayes with Genetic Algorithm, Bayesian Network | 100% |
| Dinh Ba Khanh | README and documentation | 100% |
| Tran Nguyen Anh Khoi | Github repository management | 100% |
| Tran Chi Tai | Google Colab environment setting up | 100% |



## Contributing :handshake:

Contributions are welcome! Feel free to open issues or pull requests for improvements, bug fixes, or new features.


## Acknowledgements :pray:

We would like to acknowledge the following resources and libraries that were instrumental in the development of this project:

- **Hugging Face Datasets:** For providing the IMDB dataset.
- **Scikit-learn:** For providing machine learning algorithms and tools.
- **Pgmpy:** For providing tools for working with graphical models.

## License

This project is licensed under the MIT License.


[![View on GitHub](https://img.shields.io/badge/GitHub-View_on_GitHub-blue?logo=GitHub)](https://github.com/khangtruong2252314/ML-BackProg)
