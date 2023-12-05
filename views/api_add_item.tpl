% rebase('base.tpl', title='Api_New_Item')


<form action="/apiNewItems" method="post" class='form'>
    <label for="todo" class='label has-text-centered my-3'>Task: </label>
    <input name="todo" type="text" class='input'>
    <button class='button is-fullwidth mt-3 is-primary' value="Update" type="submit">Add Task</button>

</form>