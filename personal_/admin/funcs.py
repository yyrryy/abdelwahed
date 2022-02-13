# *. .* h4
# *" "* quotes


def convertor(s):
    return s.replace("-(", "<div class=").replace(')-', '</div>').replace('-*', '<p>').replace('*-', '</p>').replace('-/', '<ul>').replace('/-', '</ul>').replace('-:', '<li>').replace(':-', '</li>').replace('-#', '<br>').replace('*.', '<h4>').replace('.*', '</h4>')

def refactor(s):
    return s.replace("<div class=", "-(").replace('</div>', ')-' ).replace('<p>', '-*' ).replace('</p>', '*-' ).replace('<ul>', '-/' ).replace('</ul>', '/-' ).replace('<li>', '-:' ).replace('</li>', ':-' ).replace('<br>', '-#' ).replace('<h4>', '*.').replace('</h4>', '.*')