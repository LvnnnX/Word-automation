from library import *

def reconcile_theme_config():
    keys = ['primaryColor', 'backgroundColor', 'secondaryBackgroundColor','textColor']
    has_changed = False
    for key in keys:
        if st._config.get_option(f'theme.{key}' != st.session_state[key]):
            st._config.set_option(f'theme.{key}', st.session_state[key])
            has_changed = True
    if has_changed:
        st.experimental_rerun()

