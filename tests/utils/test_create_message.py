def test_create_message():
    from app.utils.create_message import text_to_image
    from app.display.print_to_eink import print_img
    msg = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed quis posuere nibh, id ornare nisi. Vestibulum imperdiet id tortor ut rutrum. Etiam ac vulputate nisl. Praesent luctus porttitor blandit. Aliquam nec blandit diam. Fusce et lobortis magna. Fusce posuere consequat ipsum, et placerat odio placerat quis. Suspendisse viverra nibh id tortor tempor, eu eleifend ligula viverra. Quisque vulputate nulla enim, id vehicula est vehicula eu. Vestibulum ut porta erat, ac aliquet sapien. Aenean sagittis lacus non ipsum suscipit, in ornare purus consequat. Nullam vel congue eros. Nunc a dui nec eros consequat consequat et vel urna. Curabitur justo ligula, semper sit amet arcu id, interdum convallis tortor. Cras mollis turpis vel lacus hendrerit commodo.'
    img = text_to_image(msg)
    status = print_img(img)
    assert status['status'] == 200

