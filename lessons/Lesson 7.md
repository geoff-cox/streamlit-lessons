# st.selectbox

`st.selectbox` allows the display of a select widget.

---

## Goal of the app

1. User selects a color
2. App prints out the selected color

---

## Code

Create a new python file called `st-app-06.py`

Here's the code:

```python
import streamlit as st

st.header('st.selectbox')

option = st.selectbox(
     'What is your favorite color?',
     ('Blue', 'Red', 'Green'))

st.write('Your favorite color is ', option)
```

---

## Line-by-line explanation

We create a variable called `option` that will accept user input in the form of a **select** input widget via the `st.selectbox()` command.

```python
option = st.selectbox(
     'What is your favorite color?',
     ('Blue', 'Red', 'Green'))
```
As we can see from the above code box, the `st.selectbox()` command accepts 2 input arguments:
1. The text that goes above the select widget, i.e. `'What is your favorite color?'`
2. The possible values to select from `('Blue', 'Red', 'Green')`

Finally, we'll print out the selected color as follows:
```python
st.write('Your favorite color is ', option)
```

---

## Run the app

```
streamlit run st-app-06.py
```

---

## Demo app
Should look something like this: 

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.selectbox/)

---

## References 
More about [`st.selectbox`](https://docs.streamlit.io/library/api-reference/widgets/st.selectbox)
