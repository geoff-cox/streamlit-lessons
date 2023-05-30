# st.multiselect

`st.multiselect` displays a multiselect widget.

---

## Code

Create a new python file called `st-app-07.py`

Here's how to use `st.multiselect`:

```python
import streamlit as st

st.header('st.multiselect')

options = st.multiselect(
     'What are your favorite colors',
     ['Green', 'Yellow', 'Red', 'Blue'],
     ['Yellow', 'Red'])

st.write('You selected:', options)
```

---

## Line-by-line explanation

We use the `st.multiselect` widget to accept input where users will be able to select one or more colors of there choice.

```python
options = st.multiselect(
     'What are your favorite colors',
     ['Green', 'Yellow', 'Red', 'Blue'],
     ['Yellow', 'Red'])
```

Finally, we'll write out the selected colors:
```python
st.write('You selected:', options)
```

---

## Demo app
Should look something like this: 

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.multiselect/)

---

## Further reading
- [`st.multiselect`](https://docs.streamlit.io/library/api-reference/widgets/st.multiselect)
