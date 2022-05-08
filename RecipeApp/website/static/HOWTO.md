In order to add javascript, images, css, or any other static elements, you need to add them to this folder and then call them within some html

for example:

<body>
  <script>
    type="text/javascript"
    src="{{url_for('static', filename='index.js')}}"
  </script>
</body>

where {{}} means {{python expression}}
