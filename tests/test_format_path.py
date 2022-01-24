from invisibleroads_macros_log import format_path


def test_format_path_unix(mocker):
    home_folder = r'/home/puchica'
    mocker.patch(
        'invisibleroads_macros_log.expanduser',
        return_value=home_folder)
    assert format_path(home_folder) == '~'


def test_format_path_windows(mocker):
    home_folder = r'C:\Users\Puchica'
    mocker.patch(
        'invisibleroads_macros_log.expanduser',
        return_value=home_folder)
    assert format_path(home_folder) == '~'
