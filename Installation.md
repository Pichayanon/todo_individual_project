## Instructions for how to install and configure application

> Note : If you run the code below and find ***python : command not found***, change **python** to **python3**.

1. Clone repository from GitHub to your computer.
    ```
    git clone https://github.com/Pichayanon/todo_individual_project.git
    ```
2. Change directory to todo_individual_project.
    ```
    cd  todo_individual_project
    ```
3. Create virtual environment.
    ```
   python -m venv venv
   ```
4. Start the virtual environment.
   * macOS / Linux
     ```
     . venv/bin/activate 
     ```
   * Windows
     ```
     venv\Scripts\activate
     ```
5. Install dependencies.
   ```
   pip install -r requirements.txt
   ```
   > Note : If you can't use **pip**, change it to **pip3**.
6. Set values for externalized variables.
   * macOS / Linux
     ```
     cp sample.env .env 
     ```
   * Windows
     ```
     copy sample.env .env
     ```
7. Run migrations.
   ``` 
   python manage.py migrate
   ```
8. Run test.
   ``` 
   python manage.py test todo
   ```
   
