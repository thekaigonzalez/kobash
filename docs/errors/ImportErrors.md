# Import Errors (and how to fix them)

## Bash 

Add this line to your ~/.bashrc.

`export PYTHONPATH="${PYTHONPATH}:/path/to/my/kobash/dist."`.

So an example for me is

`export PYTHONPATH=/home/me/kobash-legacy-remake:$PYTHONPATH`

Now I can run kobash anywhere.

## Why?

Because Python has an import path system, which checks for files in directories.

Since Kobash uses the [Kobash Kernel API](../api/index.md) it needs to be able to import it.