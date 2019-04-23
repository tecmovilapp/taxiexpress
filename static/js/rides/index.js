(function ($) {
    // firestore ref
    var db;

    // auth and setup event handlers
    var init = function () {
        auth();
        $('#ContactTable').on('click', 'button.edit', edit);        
        $('#ContactTable').on('click', 'button.remove', remove);
        $('#RideAdd').click(add);
        $('#RideForm').submit(save);
    };

    // init on doc ready
    $(document).ready(init);

    // sign-in anonymously
    var auth = function () {
        firebase.auth().signInAnonymously()
        .then(function (result) {
            db = firebase.firestore();
            db.settings({ timestampsInSnapshots: true });
            list();
        })
        .catch(function (error) {
            alert("No se ha podido establecer conexión.");
        });
    };


    var listTempTr;
    // load list
    var list = function () {
        var tblBody = $('#ContactTable > tbody');
        //remove any data rows
        tblBody.find('tr.data').remove();
        //get template row
        var tempTr = tblBody.find('tr.data-temp').removeClass('data-temp').addClass('data').remove();
        if (tempTr.length) {
            listTempTr = tempTr;
        } else {
            tempTr = listTempTr;
        }

        // get collection of Rides
        // TODO: Add these filters on the Driver App
        // .where("status", "==", "passengerRequest").orderBy('requestedAt', 'asc') 
        db.collection("rides").limit(5).get().then(function (querySnapshot) {
            querySnapshot.forEach(function (doc) {
                // clone template row and append to table body
                //doc.child("requestedAt").val() = doc.child("requestedAt").val().toDate();
                var tr = tempTr.clone();
                tr.data('id', doc.id);
                var data = doc.data();
                if(data['requestedAt']){
                    data['requestedAt'] = data['requestedAt'].toDate().toLocaleString();
                }

                if(data['updatedAt']){
                    data['updatedAt'] = data['updatedAt'].toDate().toLocaleString();
                }
                
                console.log(data['requestedAt'])
                // set cell values from Contact data
                tr.find('td[data-prop]').each(function () {
                    var td = $(this);
                    td.text(data[td.data('prop')] || '');
                });
                //if(data['status'] == 'passengerRequest'){
                    tblBody.append(tr);
                //}
            });
        });
    };

    // on remove
    var remove = function (e) {
        e.preventDefault();
        if(confirm("Seguro que desea eliminar este registro?")){
            var id = $(this).parents('tr:first').data('id');
            db.collection("rides").doc(id).delete().then(function () {
                // reload list
                list();
            })
            .catch(function (error) {
                alert("Error al eliminar carrera.");
            });
        }
    };

    // on add
    var add = function (e) {
        e.preventDefault();
        open('');
    };

    // on edit
    var edit = function (e) {
        e.preventDefault();
        var id = $(this).parents('tr:first').data('id');
        open(id);
    };

    // open form modal
    var open = function (id) {
        var modal = $('#RideModal');
        // set current Contact id
        modal.data('id', id);
        // reset all inputs
        //modal.find('input').val('');
        modal.modal('show');

        if (!id){
            $('#startMap').locationpicker({
                location: {
                    latitude: 14.092546599999999,
                    longitude: -87.1861902
                },
                radius: 0,
                inputBinding: {
                    latitudeInput: $('#startLatitude'),
                    longitudeInput: $('#startLongitude'),
                    radiusInput: null,
                    locationNameInput: $('#startAddress')
                },
                enableAutocomplete: true,
                enableReverseGeocode: true,
                scrollwheel: false,
                onchanged: function (currentLocation, radius, isMarkerDropped) {
                    // Uncomment line below to show alert on each Location Changed event
                    //alert("Location changed. New location (" + currentLocation.latitude + ", " + currentLocation.longitude + ")");
                }
            });

            $('#endMap').locationpicker({
                location: {
                    latitude: 14.092546599999999,
                    longitude: -87.1861902
                },
                radius: 0,
                inputBinding: {
                    latitudeInput: $('#endLatitude'),
                    longitudeInput: $('#endLongitude'),
                    radiusInput: null,
                    locationNameInput: $('#endAddress')
                },
                enableAutocomplete: true,
                enableReverseGeocode: true,
                scrollwheel: false,
                onchanged: function (currentLocation, radius, isMarkerDropped) {
                    // Uncomment line below to show alert on each Location Changed event
                    //alert("Location changed. New location (" + currentLocation.latitude + ", " + currentLocation.longitude + ")");
                }
            });
            return;
        };

        // get Contact to edit
        db.collection("rides").doc(id).get().then(function (doc) {
            if (doc.exists) {
                var data = doc.data();
                //set form inputs from Contact data
                modal.find('input[data-prop]').each(function () {
                    var inp = $(this);
                    console.log(data[inp.data('prop')]);
                    inp.val(data[inp.data('prop')] || '');
                });

                $('#startMap').locationpicker({
                    location: {
                        latitude: $('#startLatitude').val(),
                        longitude: $('#startLongitude').val()
                    },
                    radius: 0,
                    inputBinding: {
                        latitudeInput: $('#startLatitude'),
                        longitudeInput: $('#startLongitude'),
                        radiusInput: null,
                        locationNameInput: $('#startAddress')
                    },
                    enableAutocomplete: true,
                    enableReverseGeocode: true,
                    scrollwheel: false,
                    onchanged: function (currentLocation, radius, isMarkerDropped) {
                        // Uncomment line below to show alert on each Location Changed event
                        //alert("Location changed. New location (" + currentLocation.latitude + ", " + currentLocation.longitude + ")");
                    }
                });

                $('#endMap').locationpicker({
                    location: {
                        latitude: $('#endLatitude').val(),
                        longitude: $('#endLongitude').val()
                    },
                    radius: 0,
                    inputBinding: {
                        latitudeInput: $('#endLatitude'),
                        longitudeInput: $('#endLongitude'),
                        radiusInput: null,
                        locationNameInput: $('#endAddress')
                    },
                    enableAutocomplete: true,
                    enableReverseGeocode: true,
                    scrollwheel: false,
                    onchanged: function (currentLocation, radius, isMarkerDropped) {
                        // Uncomment line below to show alert on each Location Changed event
                        //alert("Location changed. New location (" + currentLocation.latitude + ", " + currentLocation.longitude + ")");
                    }
                });

            } else {
                alert("No existe ese registro.");
            }
        }).catch(function (error) {
            alert("Error al leer carrera.");
        });
    };

    // update or add
    var save = function (e) {
        e.preventDefault();

        var modal = $('#RideModal');
        var id = modal.data('id');
        var data = {};
        //read values from form inputs
        modal.find('input[data-prop]').each(function () {
            var inp = $(this);
            data[inp.data('prop')] = inp.val();
        });

        id ? data.updatedAt = firebase.firestore.Timestamp.fromDate(new Date()) : data.requestedAt = firebase.firestore.Timestamp.fromDate(new Date());

        // update or add
        (id ? db.collection("rides").doc(id).update(data) : db.collection("rides").add(data)).then(function (result) {
            // hide modal and reload list
            modal.modal('hide');
            list();
        })
        .catch(function (error) {
            alert("Error al guardar carrera.");
        });
    };

}(jQuery));