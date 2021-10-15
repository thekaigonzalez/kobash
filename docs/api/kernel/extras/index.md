# kernel.extras

This is for extra kernel options.

Things like the Kernel Shell, Toolkit, and EcoSystem classes live here.

## Example

```python

import kernel.extras.shell as sh
import kernel.extras.toolkit as tk

sh.tmain();
tk.load_handler_script();

```