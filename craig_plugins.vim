python import sys
python import vim
python sys.path.append(vim.ecal('expand("<sfile>:h")'))

function! ConvertToDict()
python << endOfPython
from my_plugins import convert_to_dict
convert_to_dict()
endOfPython
command! ConvertToDict call ConvertToDict()
