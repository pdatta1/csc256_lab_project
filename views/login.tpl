% rebase('base.tpl', title='Login')




<div class="container is-flex-wrap-wrap mt-6">
  <form action='/' method="post">
    <div class="columns is-centered">
    <div class='column'></div>
      <div class="column">
        <h5 class='is-size-4 has-text-centered has-text-weight-bold	mb-4'>Log in here!</h5>
        <input class="input mb-3" type="text" name="username" placeholder="Username" required>
        <input class="input mb-3" type="password" name="password" placeholder="Password" required>
        <button class="button is-success" type="submit">Login</button>
      </div>
      <div class='column'></div>
    </div>
  </form>
</div>