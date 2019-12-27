function get_age(datestring){
    var dob = new Date(datestring);
    var today = new Date();
    var age = today.getFullYear() - dob.getFullYear();
    var m = today.getMonth() - dob.getMonth();
    if (m < 0 || (m == 0 && today.getDate() < dob.getDate())) {
        age--;
    }
    return age;
}

function show_remaining(e,dispID){
    var txtlength = e.value.length;
    var rem = (e.maxLength - txtlength);
    document.getElementById(dispID).textContent =  rem+'/'+e.maxLength
}

function show_image_validate(input,img_id){

    if ( ! /\.(jpe?g|png)$/i.test(input.value) )
        {
            alert('upload .jpg or .png file');
            input.value = '';
        }
        else
        {
            var filesize = input.files[0].size;
            if (filesize/1024 >8192){
                alert('Large file size. Maximum file size 7MB');
                input.value = '';
            }else{
                if (input.files && input.files[0]){
                    var reader =  new FileReader();
                    reader.onload = function(e){
                        document.getElementById(img_id).src = e.target.result;
                    };
                    reader.readAsDataURL(input.files[0])
                }
            }

        }


}