% rebase('base.tpl', title='api_update_item')

 <form action="/apiUpdateItems?todo_item={{todo_item}}" method="post">
    Task: <input name = "todo" value = "{{todo_list[todo_item]}}" type="text" />
    <input value="Update" type="submit" />
 </form>