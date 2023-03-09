from starfyre import create_component, render

from .parent import parent


def fx_app():
    return render(create_component("""
  <parent hello='world'>
      <p>{["nesting new(wrapping tags around dont work)" for i in range(4)]}</p>
  </parent>

        """))


app=fx_app()
    