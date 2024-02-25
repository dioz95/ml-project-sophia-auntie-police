# ml-project-sophia-auntie-police
This is a github repository for Machine Learning labs with Python project in Data Sciencetech Institute, Sophia batch A23. To be able to run this project, you can clone this repo and install all the required dependencies by following this procedure:
1. Clone this repo:
   ```console
   git clone <repo_url>
   ``` 
3. Create a new Conda environment:
   ```console
   conda create --name <your_env_name>
   ```
4. Activate the newly created environment:
   ```console
   conda activate <your_env_name>
   ```
6. Install the dependencies from the requirements.txt file:
   ```console
   conda install --file requirements.txt
   ```
## Files
This project consists of several files:
1. `books.csv` : Main dataset used in this project.
2. `final_notebook.ipynb` : The complete data analysis, feature engineering, modelling, and result interpretation.
3. `gbr_model_best_features.sav` : Best model from the modelling stage described in the `final_notebook.ipynb` file.
4. `app.py` : Console app to demonstrate book's rating predictor model.
5. `requirements.txt` : Required dependencies.

## How to execute this project
1. After installing the required dependencies, you can visit `final_notebook.ipynb` and run all the cells. It might take some time to finish, due to the modelling stage, depending on your machine capabilities.
2. Running `final_notebook.ipynb` will give `gbr_model_best_features.sav`, the saved model that can be used later in the deployment.
3. To see the demo, run `python app.py` in your console and follow the instructions that appear on your screen to be able to see how the model can predict the book's rating based on the given input.
