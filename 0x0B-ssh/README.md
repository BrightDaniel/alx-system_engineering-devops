# 0x0B. SSH

<table class="table table-striped">
  <thead>
    <tr>
      <th>Name</th>
      <th>Username</th>
      <th>IP</th>
      <th>State</th>
      <th></th>
    </tr>
  </thead>

  <tbody>
      <tr>
        <td>59637-web-01</td>
        <td><code>ubuntu</code></td>
        <td><code>52.23.212.37</code></td>
        <td>running</td>
        <td>
          <div class="btn-group">
            <button type="button" class="btn btn-sm btn-default dropdown-toggle" data-toggle="dropdown">
              Actions
              <span class="caret"></span>
              <span class="sr-only">Toggle Dropdown</span>
            </button>
            <ul class="dropdown-menu dropdown-menu-right">
                <li><a data-confirm="Are you sure to reboot 59637-web-01?" href="/servers/9390/soft_reboot">Soft reboot</a></li>
                  <li><a data-confirm="Are you sure to hard reboot 59637-web-01?" href="/servers/9390/hard_reboot">Hard reboot</a></li>

              <li role="separator" class="divider"></li>

                <li>
                  <a data-confirm="Are you sure you'd like a new server?
- This server will be destroyed
- Did you update your public SSH key in your user profile yet?

This action can take time...
Please, be patient..." href="/servers/9390/ask_new">
                    Ask a new server
</a>                </li>
            </ul>
          </div>
        </td>
      </tr>
    
  </tbody>
</table>
