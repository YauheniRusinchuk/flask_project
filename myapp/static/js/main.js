$(function(){
  $('.commentform_form').on('submit', (e)=>{
    e.preventDefault();
    postForm();
  })
});



function postForm() {
  $.ajax({
    url: $(this).attr('action'),
    type: 'POST',
    data: $('.commentform_text').serialize(),
    success: function(data) {
      let item = document.createElement('p')
      if(data.text){
        item.innerHTML = data.text
        $('.container_comments').append(item)
        $('.commentform_text').val('')
      }
    }
  })
}
