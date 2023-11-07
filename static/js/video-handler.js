// static/js/video-handler.js
$(document).ready(function() {
    // Fetch and display the dates
    $.getJSON('/dates', function(dates) {
      dates.forEach(function(date) {
        $('#dateList').append('<a href="#" class="list-group-item list-group-item-action" data-date="' + date + '">' + date + '</a>');
      });
  
      // Click handler for each date
      $('.list-group-item').click(function() {
        var selectedDate = $(this).data('date');
        $('#videoList').empty(); // Clear previous videos
        // Fetch and display videos for selected date
        $.getJSON('/videos/' + selectedDate, function(videos) {
          videos.forEach(function(video) {
            var videoElement = '<div class="p-2 embed-responsive embed-responsive-16by9"><video class="embed-responsive-item" controls><source src="' + '/video/' + selectedDate + '/' + video + '" type="video/mp4">Your browser does not support the video tag.</video></div>';
            $('#videoList').append(videoElement);
          });
        });
      });
    });
  });