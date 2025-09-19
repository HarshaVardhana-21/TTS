## Set virtual environment
python -m venv myenv 
.\myenv\Scripts\activate


## Install the requirements
pip install -r requirements.txt


## Run the project
uvicorn main:app --reload