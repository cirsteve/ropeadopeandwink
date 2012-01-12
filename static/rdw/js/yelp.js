var cities = {"san-francisco":{"lat":37.7721,"long":-122.4386},
              "new-york":{"lat":40.7244,"long":-73.9560},
              "los-angeles":{"lat":34.0522,"long":-118.2437},
              "chicago":{"lat":41.8755,"long":-87.6440}};
              
function getTagList(term){
  console.log('getting tags');
  console.log('tag is: ' + term);
  $('.reviews').html('');
  $('.loader').css('display','block');
  var turl = "http://api.yelp.com/business_review_search?lat=" + loc_info.lat + "&long=" + loc_info.long + "&radius=7&limit=50&ywsid=K2CVV3pYMPNNRJ6pB3-k6g&limit=15&category=" + term + "&callback=showData";
  $.ajax({
  url: turl,
  type: 'GET',
  dataType: 'jsonp',
  jsonp: false
    });
}
              
function isClosed(closed){
    if (closed === false){
        return "Open";
    }
    else {
        return "Closed";
    }
}

function sortInc(a,b){
    return parseFloat(b.avg_rating) - parseFloat(a.avg_rating);
}

function showData(data) {
    var buss = data.businesses;
    buss.sort(sortInc);
    $('.loader').css('display','none');
    var group_avg = 0;
    $.each(buss, function(i,business){
        group_avg += business.avg_rating;
        console.log(business.name + '  ' + group_avg);
        var venue = {title:{elem:'h2',content:{elem:'a',attr:{href:business.url},content:business.name}},
                    rating:{elem:'p',content:'Rating: ' + business.avg_rating},
                rating_img:{elem:'img',attr:{src:business.rating_img_url}},
                   address:{elem:'p',content:business.address1},
                    closed:{elem:'p',content:'Currently ' + isClosed(business.is_closed)},
                     photo:{elem:'img',attr:{src:business.photo_url}}
                    }
        var venue_html = '';
        var yid = 'y_' + business.id;
        var venue_d = {  title:'<div class="listing" id="' + yid + '"><h2><a href="' + business.url + '">' + business.name + '</a></h2>',
                        rating:'<div class="listing-info"><p>Rating: ' + business.avg_rating + '</p>',
                    rating_img:'<img src="' + business.rating_img_url + '" />',
                       address:'<p>' + business.address1 + '</p>',
                        closed:'<p>Currently ' + isClosed(business.is_closed) + '</p></div>',
                         photo:'<img class="listing-img" src="' + business.photo_url + '" />'
                        }
        var venue_d_str = '';
        for (var prop in venue_d){
            venue_d_str += venue_d[prop];
        }
        for (var prop in venue ){
            console.log('e: ' + prop + ' aval: ' + venue[prop] + '\n');
            if (prop === 'photo' ){
                venue_html += '<div class="listing-img"><' + venue[prop].elem + ' src="' + venue[prop].attr.src + '"/></div>';
            }
            else if (prop === 'rating_img' ){
                venue_html += '<' + venue[prop].elem + ' src="' + venue[prop].attr.src + '"/>';
            }
            else if (venue[prop].elem === 'h2'){
                venue_html += '<' + venue[prop].elem + '><' + venue[prop].content.elem + ' href="' + venue[prop].content.attr.href  + '">' + venue[prop].content.content + '</' + venue[prop].content.elem + '>' + '</' + venue[prop].elem + '>';
            }
            else if (venue[prop].elem === 'a'){
                venue_html += '<' + venue[prop].elem + ' href="' + venue[prop].attr.href + '">' + venue[prop].attr.href + '</a>';
            }
            else{
                venue_html += '<' + venue[prop].elem + '>' + venue[prop].content + '</' + venue[prop].elem + '>';
            }
        }
        console.log(venue_d_str);
        var latlg = new google.maps.LatLng(business.latitude,business.longitude);
        placeMarker(latlg,yid);
        //$('.reviews').append('<div class="listing">' + venue_html + '</div>');
        $('.reviews').append(venue_d_str);
        
        $.each(business.reviews, function(i,review){ 
            var totc = '<div class="y-review"><p><a href="' + review.url + '">' + review.text_excerpt + '</a></p>';
            totc += '<p>' + review.date + ' by ' + review.user_name + '</p></div>';
            $('.reviews .listing:last').append(totc);
        });
        $('.reviews .listing:last').find('.y-review').wrapAll('<div class="review-set" />');
        $('.reviews .listing:last .review-set').prepend('<button class="review-toggle noshow" type="button">Show Reviews</button>');
    });  
    $('.reviews').prepend('<b>Average Rating of ' + Math.round(group_avg/buss.length * 100)/100 + ' for Group of ' +  buss.length + '</b>');
    
}

