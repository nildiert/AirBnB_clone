# AirBnB Clone Shell

[![N|Solid](https://www.elfinanciero.com.mx/uploads/2019/05/07/2b8eba3cb01557277748_standard_desktop_medium_retina.png)]()

With this project that has three parts we will learn  how to create a modular application based on the AirBnB application

This is the first part, the shell. With the shell we can to manage the main functions of a database like create, update, show and delete in all the classes named in the Classes tittle
# Command interpreter
The command interpreter allows to manage data with the following methods

| Command | Function |
| ------ | ------ |
| create | Creates a new instance of a class |
| show | Shows the information of an element|
| update | Updates the information of an element |
| destroy | Deletes an instance |
| all | Shows all the elements of and instance |

## How to start it

To use this application you should clone the repository with the following command:

    git clone https://github.com/nildiert/AirBnB_clone.git
    
When clone the repository you have to enter to the directory "AirBnB":

    cd AirBnB
    
Inside the directory, execute the file "console":

    ./console

## How to use it

### Interactive mode
For the interactive mode you should execute the command "./console"

    ./console
    (hbnb)

### Non interactive mode

To use the non-interactive mode you must use the echo command and inside quotes the interpreter's instructions then use a pipe with the name of the file (./console).

    echo "create BaseModel" | ./console
    (hbnb) b55d9817-62f5-4554-bdaf-24e7a83ad9a3
    (hbnb)
    
### Commands


* [create]() - To use this command you need to write "create" and then the name of the class. Note that you can only create an object of the classes named at the bottom of this file.
```
    create BaseModel
    843497da-f9c5-4ffc-bdf3-1a6b68f74702
```    
* [show]() - To use this command you need to write "show", the name of the class and the id. You must write all the data previously requested
```
show BaseModel 843497da-f9c5-4ffc-bdf3-1a6b68f74702
[BaseModel] (843497da-f9c5-4ffc-bdf3-1a6b68f74702) {'created_at': datetime.datetime(2019, 7, 2, 18, 34, 35, 37016), 'id': '843497da-f9c5-4ffc-bdf3-1a6b68f74702', 'updated_at': datetime.datetime(2019, 7, 2, 18, 34, 35, 37138)}
(hbnb) show
** class name missing **
(hbnb)
(hbnb) show BaseModel
** instance id missing **
(hbnb)
```

* [update]() - To use this command you need to write "update", the name of the class, the id, the name of the attribute and the value. You must write all the data previously requested
```
(hbnb) update BaseModel b6f2ef1d-9673-47c5-ab4e-44eff3d05e9f user Nildiert
(hbnb) show BaseModel b6f2ef1d-9673-47c5-ab4e-44eff3d05e9f)
[BaseModel] (b6f2ef1d-9673-47c5-ab4e-44eff3d05e9f) {'updated_at': datetime.datetime(2019, 7, 2, 20, 35, 24, 853837), 'user': 'Nildiert', 'created_at': datetime.datetime(2019, 7, 2, 17, 2, 52, 520693), 'id': 'b6f2ef1d-9673-47c5-ab4e-44eff3d05e9f'}
(hbnb)
```
* [destroy]() - To use this command you need to write "destroy", the name of the class and the id.
```
(hbnb) destroy BaseModel b6f2ef1d-9673-47c5-ab4e-44eff3d05e9f
(hbnb) show BaseModel b6f2ef1d-9673-47c5-ab4e-44eff3d05e9f
** no instance found **
(hbnb) 
```
* [all]() - To use this command you need to write "all", and the name of the class.
```
[BaseModel] (843497da-f9c5-4ffc-bdf3-1a6b68f74702) {'created_at': datetime.datetime(2019, 7, 2, 18, 34, 35, 37016), 'id': '843497da-f9c5-4ffc-bdf3-1a6b68f74702', 'updated_at': datetime.datetime(2019, 7, 2, 18, 34, 35, 37145)}
[BaseModel] (843497da-f9c5-4ffc-bdf3-1a6b66f8475 {'created_at': datetime.datetime(2019, 7, 2, 18, 34, 35, 37016), 'id': '843497da-f9c5-4ffc-bdf3-1a6b66f84755', 'updated_at': datetime.datetime(2019, 7, 2, 18, 34, 35, 37145)}
```

## Classes

We will manipulate the information in different classes:

  - User
  - State
  - Amenity
  - Place
  - Review
  
#### Holberton school cohort 8 - Bogotá

See [Holberton School](https://www.holbertonschool.com/)

### Collaborators

 - Nildiert Jimenez
 - Javier Bonilla

