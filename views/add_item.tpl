% rebase('base.tpl', title='New_Item')


<form action="/newItems" method="post" class='form'>
    <label for="todo" class='label has-text-centered my-3'>Task: </label>
    <input name="todo" type="text" class='input'>
    <button class='button is-fullwidth mt-3 is-primary' value="Update" type="submit">Add Task</button>

</form>