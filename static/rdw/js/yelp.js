var cities = {"san-francisco":{"lat":37.7721,"long":-122.4386},
              "new-york":{"lat":40.7244,"long":-73.9560},
              "los-angeles":{"lat":34.0522,"long":-118.2437},
              "chicago":{"lat":41.8755,"long":-87.6440}}

function showData(data) {
    var buss = data.businesses;
    $('.loader').css('display','none');
    $('.reviews').append('<b>Total Venues: ' +  buss.length + '</b>');
    $.each(buss, function(i,business){
        console.log(business.name);
        var tot = '<h2>' + business.name + '</h2><p>Average Rating: ' + business.avg_rating + ' Address ' + business.address1 + '</p>';
        var latlg = new google.maps.LatLng(business.latitude,business.longitude);
        placeMarker(latlg);
        $('.reviews').append(tot);
        $.each(business.reviews, function(i,review){ 
            var totc = '<p>' + review.text_excerpt + '</p>';
            totc += '<p>' + review.date + ' by ' + review.user_name + '</p>';
            //$(content).appendTo('#review');
            $('.reviews').append(totc);
        });
    });  
}

function getTagList(term){
  console.log('getting tags');
  console.log('city is:  & ' + term);
  $('.reviews').html('');
  $('.loader').css('display','block');
  var turl = "http://api.yelp.com/business_review_search?term=" + term + "&lat=" + loc_info.lat + "&long=" + loc_info.long + "&radius=10&limit=50&ywsid=K2CVV3pYMPNNRJ6pB3-k6g&limit=15&callback=showData";
  $.ajax({
  url: turl,
  type: 'GET',
  dataType: 'jsonp',
  jsonp: false
    });
}