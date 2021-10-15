# kernel.security

Information about the base computer.

## Example

```py

import kernel.security.mask as mask

mask.pure_user() #-> kai
mask.generate_home() #-> make directory home/kai (NOT ~)
```