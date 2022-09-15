function submit(e)
{
    e.preventDefault();
    var out1 = document.getElementById('a').value;
    var out2 = document.getElementById('b').value;
    var out3 = document.getElementById('c').value;
    window.open('', 'formpopup', 'width=400,height=400,resizeable,scrollbars');
    wdw.document.body.textContent = out1 + ' \n' + out2+'\n'+out3;

        
}