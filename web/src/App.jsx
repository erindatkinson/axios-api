import { useEffect, useState } from 'react';
import Todo from "./components/Todo";
import FilterButton from './components/FilterButton';
import Form from './components/Form';
import './App.css'
import API from './api';
import { nanoid } from 'nanoid';

const FILTER_MAP = {
    All: () => true,
    Active: (task) => !task.completed,
    Completed: (task) => task.completed,
}
const FILTER_NAMES = Object.keys(FILTER_MAP);

function App(props) {
    const [tasks, setTasks] = useState([]);
    const [filter, setFilter] = useState("All");

    useEffect(() => {
        API.get(`tasks`)
            .then(res => {
                const tempTasks = res.data;
                setTasks(tempTasks);
            }).catch(err => {
                console.error(err);
            });


    }, []);

    function toggleTaskCompleted(id) {
        const updatedTasks = tasks.map((task) => {
            if (id === task.id) {
                API.patch(`tasks/${id}`, { completed: !task.completed })
                    .then(resp => {
                        console.log(resp);
                    })
                    .catch(err => {
                        console.error(err);
                    });
                return { ...task, completed: !task.completed }
            }
            return task
        });
        setTasks(updatedTasks);
    }

    function editTask(id, newName) {
        const editedTaskList = tasks.map((task) => {
            if (id === task.id) {
                let editedTask = API.patch(`tasks/${id}`, { name: newName })
                    .then(resp => {
                        return resp
                    })
                    .catch(err => {
                        console.error(err);
                        return task;
                    });
                console.log("edited task" + editedTask);
                return { ...task, name: newName };
            }
            return task;
        })
        setTasks(editedTaskList);
    }

    function deleteTask(id) {
        const remainingTasks = tasks.filter((task) => id !== task.id);
        API.delete(`tasks/${id}`)
            .then(resp => {
                console.log(resp);
                setTasks(remainingTasks);
            })
            .catch(err => {
                console.error(err);
            });
    }

    const taskList = tasks.filter(FILTER_MAP[filter])
    .map((task) => (
        <Todo
            key={task.id}
            id={task.id}
            name={task.name}
            completed={task.completed}
            toggleTaskCompleted={toggleTaskCompleted}
            deleteTask={deleteTask}
            editTask={editTask} />));

    const filterList = FILTER_NAMES.map((name) => (
        <FilterButton
            key={name}
            name={name}
            isPressed={name === filter}
            setFilter={setFilter} />))

    function addTask(name) {
        const newTask = { id: `todo-${nanoid()}`, name, completed: false };
        setTasks([...tasks, newTask]);
        API.post(`tasks`, newTask)
            .then(resp => {
                console.log(resp);
            }).catch(err => {
                console.error(err);
            })
    }

    const headingNoun = taskList.length !== 1 ? "tasks" : "task";
    const headingText = `${taskList.length} ${headingNoun} remaining`

    return (
        <div className='todoapp stack-large'>
            <h1>TodoMatic</h1>
            <Form onSubmit={addTask} />
            <div className='filters btn-group stack-exception'>
                {filterList}
            </div>
            <h2 id='list-heading'>{headingText}</h2>
            <ul
                role='list'
                className='todo-list stack-large stack-exception'
                aria-labelledby='list-heading'>

                {taskList}
            </ul>
        </div>
    );
}

export default App
