<h1> Dictionary API </h1>

<h3>Overview</h3> 

This API allows users to create, update, read, and delete custom dictionaries, as well as translate words according to the specific dictionary definitions provided. It's built using FastAPI and relies on SQLAlchemy for database interactions, supporting MySQL as the database backend.

<h3>Features</h3> 

- **Create Dictionaries:** Users can create their own dictionaries with custom definitions.
- **Read Dictionaries:** Access details of the existing dictionaries.
- **Update Dictionaries:** Modify the content of existing dictionaries.
- **Delete Dictionaries:** Remove dictionaries no longer needed.
- **Translate Words:** Translate words using the created dictionaries.

<h3>Requirements</h3> 

- **FastAPI**
- **Uvicorn** (for running the FastAPI app)
- **Pydantic** (for data validation)
- **SQLAlchemy** (for database interaction)
- **MySQLClient** (for MySQL database support)

<h3>Setup Instructions</h3> 

```bash
git clone https://github.com/votre_username/votre_projet.git
```
Navigate to the project directory and run:
```bash
pip install -r requirements.txt```
```
Set up the MySQL database:

    Ensure you have MySQL installed and running.
    Create a database named sf-react.

Configure the application:
Update database.py to reflect your database credentials and connection details.

Run the application:
```bash
uvicorn main:app --reload
```
<h3>Docker Support</h3> 

This project includes Dockerfile and docker-compose.yml files for easy containerization and deployment. To use Docker, ensure you have Docker and Docker-Compose installed, then run:

 ```bash
     docker-compose up --build
```
This will build the Docker image and start the service, making the API accessible.

<h3>Contributing</h3> 
Contributions to the Dictionary API are welcome. Please ensure to follow the existing code style and add unit tests for any new or changed functionality.
