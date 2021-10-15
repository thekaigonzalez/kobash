# Import Errors (and how to fix them)

## Bash 

Add this line to your ~/.bashrc.

`export PYTHONPATH="${PYTHONPATH}:/path/to/my/kobash/dist."`.

So an example for me is

`export PYTHONPATH=/home/me/kobash-legacy-remake:$PYTHONPATH`

Now I can run kobash anywhere.