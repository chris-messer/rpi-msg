import textwrap

def wrap_text(msg):
    wrapped_msg_list = textwrap.wrap(
        msg,
        width=30,
        max_lines=7,
        placeholder="...")

    wrapped_msg = '\n'.join(wrapped_msg_list)
    return wrapped_msg