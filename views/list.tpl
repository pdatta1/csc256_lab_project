% rebase('base.tpl', title='list')


<form id='todo_form' class=' columns'>

    <div class='field is-grouped is-flex-direction-column column'>
        <button class="side-bar button is-primary is-light is-hovered" type="button" onclick="processForm('add')">Add New Item</button>

        <button class='side-bar button is-warning is-light ' type="button" onclick="processForm('update')">Update Item</button>

        <button class="side-bar button is-danger is-light " type="button" onclick="processForm('delete')">Delete Item</button>

        <button class="side-bar button is-info is-light " type="button" onclick="processForm('sort')">Sort Items</button>
    </div>
    
    <div class='column'>
        % for task in range(len(todo_list)):
            %if task == 0:
                <input class='radio my-2' type="radio" name="todo_item" value="{{task}}" checked="checked"> {{todo_list[task]}} </br>
            % else:
                <input class='radio my-2' type="radio" name="todo_item" value="{{task}}"> {{todo_list[task]}} </br>
            % end
        % end
    </div>

</form>