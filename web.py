import streamlit as st
import functions

st.title("My Todo App:")

todos = functions.get_todos()
def add_todo():
    new_todo = st.session_state["todo"] + "\n"
    todos.append(new_todo)
    functions.write_todos(todos)


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()
input_box = st.text_input(label="", placeholder="Enter a todo",
                         on_change=add_todo, key="todo")
