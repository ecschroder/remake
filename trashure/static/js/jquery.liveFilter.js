/***********************************************************/
/*                    LiveFilter Plugin                    */
/*                      Version: 1.1                       */
/*                      Mike Merritt                       */
/*             	    Updated: Feb 2nd, 2010                 */
/***********************************************************/

(function($){
	$.fn.liveFilter = function (wrapper) {

		// Grabs the id of the element containing the filter
		var wrap = '#' + $(this).attr('id');

		// Make sure we're looking in the correct sub-element
		if (wrapper == 'table') {
			var item = 'tr';
		} else {
			var item = 'li';
		}

		// Listen for the value of the input to change
		$('input.filter').keyup(function() {
			var filter = $(this).val();

			// Hide all the items and then show only the ones matching the filter
			$(wrap + ' ' + wrapper + ' ' + item).hide().addClass("ding-ding-ding");

			if (wrapper == 'table') {
				$(wrap + ' ' + wrapper + ' ' + 'tr.header').show();
			}
			$(wrap + ' ' + wrapper + ' ' + item + ':Contains("' + filter + '")').show();

		});

		// Custom expression for case insensitive contains()
		jQuery.expr[':'].Contains = function(a,i,m){
		    return jQuery(a).text().toUpperCase().indexOf(m[3].toUpperCase())>=0;
		};

	}

})(jQuery);