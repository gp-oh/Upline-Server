// Written for jQuery
$(function(){
    function toggle_notifications(){
        if ( $('#id_have_notifications').prop('checked')) {
            $(".field-count_messages_after_finish").show();
            $(".field-day_1_notification_description").show();
            $(".field-day_2_notification_description").show();
            $(".field-day_3_notification_description").show();
            $(".field-day_4_notification_description").show();
            $(".field-day_5_notification_description").show();
            $(".field-day_6_notification_description").show();
            $(".field-day_7_notification_description").show();
            $(".field-day_14_notification_description").show();
            $(".field-day_28_notification_description").show();
        } else {
            $(".field-count_messages_after_finish").hide();
            $(".field-day_1_notification_description").hide();
            $(".field-day_2_notification_description").hide();
            $(".field-day_3_notification_description").hide();
            $(".field-day_4_notification_description").hide();
            $(".field-day_5_notification_description").hide();
            $(".field-day_6_notification_description").hide();
            $(".field-day_7_notification_description").hide();
            $(".field-day_14_notification_description").hide();
            $(".field-day_28_notification_description").hide();
        }
    }
    function toggle_answers(){
        if ( $('#id_need_answer').prop('checked')) {
            $('.field-answer_type').show();
        } else {
            $('.field-answer_type').hide();
            $('.field-meetings_per_week').hide();
            $('.field-weeks').hide();
            $('.field-nr_contacts').hide();
        }
    }

    function toggle_aswer_type() {
        $('.field-meetings_per_week').hide();
        $('.field-weeks').hide();
        $('.field-nr_contacts').hide();
        if ($('#id_answer_type').val() == 3) {
            $('.field-nr_contacts').show();
        } else if ($('#id_answer_type').val() == 4) {
            $('.field-meetings_per_week').show();
            $('.field-weeks').show();
        };
    }
    toggle_notifications();
    toggle_answers();
    toggle_aswer_type();
    // on page load...
    $('#id_have_notifications').change(function(){
        toggle_notifications();
    });
    $('#id_need_answer').change(function(){
        toggle_answers();
    });
    $('#id_answer_type').change(function(event) {
        toggle_aswer_type();
    });

});
