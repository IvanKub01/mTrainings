

$(function () {
    $('#findbut').click(function () {
        var ix = $("#trans").prop("selectedIndex");
        console.log(ix);
        $('#DMTdiv').toggle(ix === 0);
        $('#Ayawaskadiv').toggle(ix === 1);
    });

    $("#findzoznam").on('click', function () {
        iddd = "dd"
        $.ajax({
            url: '/printZoznam',
            data: {
                'iddd': iddd,


            },
            type: 'GET',
            success: function (data) {

                data = JSON.parse(data);

                var lenght = Object.keys(data).length;
                console.log("length " + lenght)
                $("#zoznam_body").empty();

                for (var i = 0; i < lenght; i++) {
                    $("#zoznam_body")
                        .append($('<tr>'))
                    string1 = "";

                    Object.keys(data[i]).forEach(function (key) {
                        if (key == 'idcko') {
                            string1 = data[i][key];
                        } else {
                            $("#zoznam_body").last('tr')
                                .append($('<td class="pl-3 feedb-text " name=' + string1 + ' >')
                                    .text(data[i][key])
                                )
                        }
                    })
                    $("#zoznam_body").last('tr')
                        .append($('<td><button id= "' + string1 + '" type="button" class="btn btn-sm text-center w-100 h-100 btn-danger d-inline-block deleteBox "><i class="fas fa-trash-alt"></i></button></td>'))
                        .append($('<td><button data-toggle="modal" data-target="#myModal" value= "' + string1 + '" type="button" class="btn btn-sm text-center w-100 h-100 btn-primary d-inline-block editBox "><i class="far fa-edit"></i></button></td>'))
                }
            },
            error: function () {
                console.log("ajax error");
            }
        });

    })
    function checkNick(nick) {
        var ok = 0
        $.ajax({
            url: '/readNick',
            async: false,
            data: {
                'idNick': nick

            },

            type: 'GET',
            success: function (jify) {

                if (!(isEmpty(jify))) {
                    alert("Osoba z daným Nickom už je v Databáze ! ");
                    ok = 1;
                }
            },
            error: function () {
                console.log("ajax error");
            }
        });
        return ok;
    };

    $("#AddNickANum").on('click', function () {

        idNick = $("#IDNick").val();
        IDpass = $("#IDpass").val();
        IDpass2 = $("#IDpass2").val();
        IDpass = IDpass.toString();
        IDpass2 = IDpass2.toString();
        num = checkNick(idNick);
        console.log(num);
        var ll = IDpass2.length
        console.log(ll)
        //if ((IDpass === IDpass2) && (!isEmpty(idNick)) && (!isEmpty(IDpass)) && (num === 0)) {
        if (num === 0) {
            if (IDpass === IDpass2) {
                if ((!isEmpty(idNick)) && (!isEmpty(IDpass))) {
                    if (ll > 4) {
                        //console.log(idNick);
                        //console.log(IDpass);            
                        //console.log(IDpass2);
                        $.ajax({
                            url: '/insertNick',
                            data: {
                                'idNick': idNick,
                                'IDpass': IDpass
                            },

                            type: 'POST',
                            success: function (x) {

                                alert("Nick '" + x + "' bola pridaná!")

                            },
                            error: function (x) {
                                console.log("insert error");
                                alert("Nick '" + x + "' nebola pridaná!")
                            }
                        });
                    } else {
                        alert("Heslo musí mat od 5 do 8 znakov")
                    }
                } else {
                    alert("Nezadali ste niektory z parametrov!")
                }
            } else {
                alert("Hesla sa nerovnaju!")
            }
        }
    })




    function isEmpty(obj) {
        return Object.keys(obj).length === 0;
    }



    $(document).on('click', ".deleteBox", function () {

        Mystring = "";
        Mystring = $(this).attr('id');


        $.ajax({
            url: '/delIDfun',
            data: {
                'delID': Mystring
            },
            type: 'DELETE',
            success: function () {
                $('#findzoznam').trigger('click');
                alert("Zmazané!");

            },
            error: function () {
                console.log("ajax error");
            }
        });
    })

    $(document).on("click", "#closemodal", function () {

        $('#myModal').hide();
    });
    $(document).on("click", "#okModal", function () {
        $('#myModal').hide();
    });
    // ++++++++++++++++++++++++++++++++++++++++++++++++++edit+++++++++++++++++++++++++++++++++++++++++++++++++++++
    $(document).on('click', ".editBox", function () {

        idckyy = "";
        idckyy = $(this).attr('value');
        console.log(idckyy);

    })


    $("#okModal").on('click', function () {


        nick = $("#nickM").val();
        password = $("#passwordM").val();
        psslen = password.length
        console.log(psslen)
        if (!(isEmpty(nick))) {
            if (psslen > 4) {
                $.ajax({
                    url: '/updateTerm',
                    data: {
                        'id': idckyy,
                        'nick': nick,
                        'password': password,

                    },

                    type: 'PUT',
                    success: function (x) {
                        alert("polozka bola editovana :" + x)
                        $('#findzoznam').trigger('click');
                    },
                    error: function (x) {
                        console.log("update error");
                        alert("nedosla ku editovaniu")

                    }

                });
            } else {
                alert("Heslo musí mat od 5 do 8 znakov")
            }
        } else {
            alert("Nezadali ste nick")
        }
    })




});
