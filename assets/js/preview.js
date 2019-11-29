function Editor(input, preview) {
  console.log(input);
  this.update = function() {
    preview.innerHtml = markdown.toHTML(input.value);
  };
  input.editor = this;
  this.update();
}
django.jQuery(document).ready(function() {
  new Editor(django.jQuery("#id_descriotion")[0], django.jQuery("#preview")[0]);
});
