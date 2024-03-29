from skimpy.skimpy import Skimpy

expected_output = """\
<!DOCTYPE html>
<body>
 <div id="menu">
  <a href="/auth/login">
   Login
  </a>
 </div>
</body>
"""

vars = {
    'login_path': '/auth/login',
}

# breakpoint()

def test_sub_templates():
    skimpy = Skimpy('tests/fixtures/basic_template.skml', vars = vars, pretty = True)
    output = skimpy.render()
    skimpy.debug()

    assert output == expected_output
