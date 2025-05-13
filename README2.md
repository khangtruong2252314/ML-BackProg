---

# ML-ClassicalModels

This project explores various classical Machine Learning techniques for classification and ensemble modeling. It includes implementations of Support Vector Machines (SVMs), Dimension Reduction techniques (PCA and LDA), Bagging and Boosting methods, and Discriminative models including Logistic Regression, Entropy-based models, and Conditional Random Fields (CRF).

## Dataset \:bar\_chart:

This project uses curated datasets *pneumonia* suitable for binary or multi-class classification tasks. Each dataset contains feature vectors and corresponding labels. The dataset is available on Kaggle, via the [link](https://www.kaggle.com/datasets/paultimothymooney/chest-xray-pneumonia) 

## Models \:robot:

The following models are implemented and evaluated:

* **Support Vector Machine (SVM):** Implements various kernel functions (linear, polynomial, RBF) and explores the impact of soft vs. hard margin classifiers. The optimization seeks a hyperplane that maximizes margin between classes while controlling slack via regularization.

* **Dimension Reduction:**

  * **PCA (Principal Component Analysis):** An unsupervised technique that projects data into lower dimensions by preserving maximal variance.
  * **LDA (Linear Discriminant Analysis):** A supervised technique that maximizes class separability by projecting onto a space that best discriminates classes.

* **Bagging and Boosting:**

  * **Bagging (Bootstrap Aggregating):** Trains multiple base classifiers (e.g., decision trees) on bootstrapped subsets and aggregates their predictions (e.g., majority voting).
  * **Boosting:** Sequentially trains weak learners, each focusing more on previous errors (e.g., AdaBoost), to improve overall accuracy.

* **Discriminative Models:**

  * **Logistic Regression:** Estimates the probability of class membership using a sigmoid on linear predictors.
  * **Entropy-based Model:** (Further clarification needed—likely refers to maximum entropy or information gain criteria).
  * **CRF (Conditional Random Fields):** A structured prediction model that estimates the conditional probability of label sequences given an observation sequence, widely used in NLP tasks.

## Usage \:rocket:

1. **Install Dependencies:** Install required libraries using `pip install -r requirements.txt`.
2. **Run Models:** Scripts or Jupyter notebooks are provided for training and evaluating each model.
3. **Visualize Results:** Evaluation includes metrics such as accuracy, precision, recall, and visualization via confusion matrices and projection plots.

## Results \:clipboard:

| Model               | Task                          | Notes                                                        |
| ------------------- | ----------------------------- | ------------------------------------------------------------ |
| SVM (Linear, RBF)   | Classification                | High performance on linearly and non-linearly separable data |
| PCA, LDA            | Dimensionality Reduction      | Used as preprocessing or visualization step                  |
| Bagging             | Ensemble                      | Reduces variance, robust to overfitting                      |
| Boosting            | Ensemble                      | Increases accuracy, sensitive to noise                       |
| Logistic Regression | Discriminative Classification | Simple and interpretable                                     |
| Entropy-based       | Exploratory                   | Entropy criteria for split or prediction (details may vary)  |
| CRF                 | Sequence Classification       | Useful for structured output problems                        |

## Team Members and Their Contributions \:busts\_in\_silhouette:

| Team Member | Contribution                                  | Distribution |
| ----------- | --------------------------------------------- | ------------ |
| Truong Minh Khang    | SVM, Bagging, Boosting                        | 100%         |
| Nguyen Minh Khoi    | PCA, LDA, Logistic Regression                 | 100%         |
| Dinh Ba Khanh    | CRF, Entropy model                            | 100%         |
| Tran Nguyen Anh Khoi    | Documentation & results visualization         | 100%         |
| Tran Chi Tai    | Project environment setup & GitHub management | 100%         |

## Contributing \:handshake:

Contributions are welcome! Please feel free to submit pull requests or open issues for any improvements or suggestions.

## Acknowledgements \:pray:

We gratefully acknowledge the following libraries and resources:

* **Scikit-learn:** For core ML models and utilities.
* **NumPy / SciPy / Pandas:** For numerical computations and data processing.
* **Matplotlib / Seaborn:** For plotting and result visualization.

## License

This project is licensed under the MIT License.

[![View on GitHub](https://img.shields.io/badge/GitHub-View_on_GitHub-blue?logo=GitHub)](https://github.com/khangtruong2252314/ML-BackProg)

---
