function formValidation()
{
var uid = document.registration.book_id;
var mobile_no = document.registration.m_number;
if(bookid_validation(uid,1,5))
{
if(mobile_no_validation(mobile_no,10))
{
    return true;
}
}

}
function bookid_validation(uid,mx,my)
{
var uid_len = uid.value.length;
if (uid_len == 0 || uid_len >= my || uid_len < mx)
{
alert("Book Id should not be empty / between 0 to 9999");
uid.focus();
return false;
}
return true;
}
function mobile_no_validation(mobile_no,mx)
{
var mobile_no_len = mobile_no.value.length;
if (mobile_no_len != mx)
{
alert("Mobile Number should not be empty /  must be "+mx +"digit number");
mobile_no.focus();
return false;
}
return true;
}