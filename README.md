# ML-BackProg

This project explores various Machine Learning models for sentiment classification on the IMDB dataset. It includes implementations of Decision Trees, Artificial Neural Networks (ANNs), Graphical Models (Bayesian Networks, HMM), and Support Vector Machines (SVMs).

## Dataset :bar_chart:

The project utilizes the [IMDB dataset](https://huggingface.co/datasets/stanfordnlp/imdb) from Hugging Face Datasets. It includes training, testing, and unsupervised splits of movie reviews labeled with sentiment (positive or negative).

## Models :robot:

The following models are implemented and evaluated:

- **Decision Tree:** A classic tree-based model for classification.
- **ANN:** A feedforward neural network using scikit-learn's MLPClassifier.
- **Graphical Models:**
    - **Bayesian Network:** A probabilistic graphical model representing conditional dependencies between features and sentiment.
    - **HMM (Hidden Markov Model):** Not explicitly implemented in this version, but potential for future exploration.
- **Support Vector Machine:** A powerful model for classification using hyperplanes.
- **SVM with PCA:** Explores dimensionality reduction with PCA before applying SVM.

## Usage :rocket:

1. **Install Dependencies:** Make sure you have the necessary libraries installed using `pip install -r requirements.txt`.
2. **Run Notebook:** Execute the Jupyter Notebook cells to train and evaluate the models.
3. **Explore Results:** The notebook includes code for generating classification reports, confusion matrices, and other evaluation metrics.


## Results :clipboard:

| Model | Accuracy | Precision | Recall | F1-Score |
|---|---|---|---|---|
| Decision Tree | 0.85 | 0.86 | 0.84 | 0.85 |
| ANN | 0.88 | 0.89 | 0.87 | 0.88 |
| Naive Bayes | 0.84| 0.84 | 0.84 | 0.84 |
| Bayesian Network | 0.75 | 0.76 | 0.74 | 0.75 |
| HMM | 0.87 | 0.88 | 0.86 | 0.87 |

**Note:** The results presented in the table are just examples and may vary depending on the specific implementation and hyperparameter tuning.


## Team Members and Their Contributions :busts_in_silhouette:

| Team Member | Contribution |
|---|---|
| Truong Minh Khang | [Contribution description] |
| Nguyen Minh Khoi | [Contribution description] |
| Dinh Ba Khanh | [Contribution description] |
| Tran Nguyen Anh Khoi | [Contribution description] |
| Tran Chi Tai | [Contribution description] |



## Contributing :handshake:

Contributions are welcome! Feel free to open issues or pull requests for improvements, bug fixes, or new features.


## Acknowledgements :pray:

We would like to acknowledge the following resources and libraries that were instrumental in the development of this project:

- **Hugging Face Datasets:** For providing the IMDB dataset.
- **Scikit-learn:** For providing machine learning algorithms and tools.
- **Pgmpy:** For providing tools for working with graphical models.

## License

This project is licensed under the MIT License.


[![View on GitHub](https://img.shields.io/badge/GitHub-View_on_GitHub-blue?logo=GitHub)](your_repository_link) 

**Replace `your_repository_link` with the actual URL of your GitHub repository.**
