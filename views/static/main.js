function processForm(action) {
    let form = document.getElementById('todo_form');
    let selectedRadio = document.querySelector('input[name="todo_item"]:checked');
    let selectedValue = selectedRadio ? selectedRadio.value : null;

    switch (action) {
        case 'add':
            form.action = '/newItems';
            break;
        case 'update': form.action = '/updateItems?todo_item=' + selectedValue;
            break;
        case 'delete':
            form.action = '/deleteItems?todo_item=' + selectedValue;

    }

    form.submit();
}