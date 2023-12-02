% rebase('base.tpl', title='update_item')

 <form action="/updateItems?todo_item={{todo_item}}" method="post">
    Task: <input name = "todo" value = "{{todo_list[todo_item]}}" type="text" />
    <input value="Update" type="submit" />
 </form>