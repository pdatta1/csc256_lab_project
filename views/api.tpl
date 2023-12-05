% rebase('base.tpl', title='api')

<h2>API PAGE</h2>
<form id='todo_form' class=' columns'>

    <div class='field is-grouped is-flex-direction-column column'>
        <button class="side-bar button is-primary is-light is-hovered" type="button" onclick="processApiForm('add')">Add New Item</button>

        <button class='side-bar button is-warning is-light ' type="button" onclick="processApiForm('update')">Update Item</button>

        <button class="side-bar button is-danger is-light " type="button" onclick="processApiForm('delete')">Delete Item</button>

        <button class="side-bar button is-info is-light " type="button" onclick="processApiForm('sort')">Sort Items</button>

        <button class="side-bar button is-success is-light " type="button" onclick="processApiForm('json')">Generate Json</button>

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