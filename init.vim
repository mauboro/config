:set number
:set relativenumber
:set autoindent
:set tabstop=4
:set shiftwidth=4
:set softtabstop=4
:set mouse=a
:set termguicolors

call plug#begin()

Plug 'morhetz/gruvbox'
let g:airline_theme='gruvbox'
Plug 'https://github.com/preservim/nerdtree'
Plug 'https://github.com/vim-airline/vim-airline'
Plug 'http://github.com/vim-airline/vim-airline-themes'
Plug 'Yggdroot/indentLine'
let g:indentLine_concealcursor = 'inc'
let g:indentLine_conceallevel = 2
let g:indentLine_char_list = ['|', '¦', '┆', '┊']
Plug 'mattn/emmet-vim'
Plug 'https://github.com/tpope/vim-commentary'
Plug 'neoclide/coc.nvim', {'branch': 'release'}
Plug 'ThePrimeagen/vim-be-good'
set encoding=UTF-8

call plug#end()

colorscheme gruvbox

nnoremap <C-f> :NERDTreeFocus<CR>
nnoremap <C-n> :NERDTree<CR>
nnoremap <C-t> :NERDTreeToggle<CR>


" for html/rb files, 2 spaces
autocmd Filetype html setlocal ts=2 sw=2 

" highlight Normal guibg=none
" highlight NonText guibg=none

" highlight Normal ctermbg=none
" highlight NonText ctermbg=none

" inoremap <silent><expr> <TAB>
"       \ coc#pum#visible() ? coc#pum#next(1) :
"       \ CheckBackspace() ? \<Tab>" :
"       \ coc#refresh()
" inoremap <expr><S-TAB> coc#pum#visible() ? coc#pum#prev(1) : \<C-h>"


