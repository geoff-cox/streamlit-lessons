---

## The button object

`st.button` allows the display of a button widget.

---

## Goal of the app:

1. By default, the app prints `Goodbye`
2. Upon clicking on the button, the app displays the alternative message `Why hello there`

---

## Code

Create a new python file called `st-app-02.py`

Here's the code for the app:

```python
import streamlit as st

st.header('st.button')

if st.button('Say hello'):
     st.write('Why hello there')
else:
     st.write('Goodbye')
```

---

## Line-by-line explanation

The very first thing to do when creating a Streamlit app is to start by importing the `streamlit` library as `st` like so:

```python
import streamlit as st
```

This is followed by creating a header text for the app:

```python
st.header('st.button')
```

Next, we will use conditional statements `if` and `else` for printing alternative messages.

```python
if st.button('Say hello'):
     st.write('Why hello there')
else:
     st.write('Goodbye')
```

As we can see from the above code box, the `st.button()` command accepts the `label` input argument of `Say hello`, which is the text that the button displays.

The `st.write` command is used to print text messages of either `Why hello there` or `Goodbye` depending on whether the button was clicked or not, which is implemented via:


```python
st.write('Why hello there')
```

and

```python
st.write('Goodbye')
```

It is important to note that the above `st.write` statements are placed under the `if` and `else` conditions in order to perform the above mentioned process of alternative displaying of messages

---

### Run the app

Click on the terminal tab at the bottom of the PyCharm interface. 

In the terminal, enter the following:

```
streamlit run st-app-02.py
```
