mkdir -p ~/. streamlit/

echo "\
[server]\n\
port = $PORT\n\
enableCORs = false n\
headless = true \n\
\n\

" > ~/.streamLit/config.toml
