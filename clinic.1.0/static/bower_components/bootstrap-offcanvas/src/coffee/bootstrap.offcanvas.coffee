# Only one navbar should have touch enabled
# More than one would cause confusion on the page
# This variable is true if touch is already enabled or false if not
touch = false

class OffcanvasDropdown
    #   Public: Constructor for offcanvas
    #
    #   @element - Element that toggles the offcanvas
    constructor: (@element) ->
        @element = $ @element

        # Get dropdown element
        @dropdown = @element.parent().find ".dropdown-menu"

        # Click event
        @element.on 'click', @_clickEvent

    #   Private: Click event on link
    _clickEvent: (e) =>
        e.preventDefault() if !@dropdown.hasClass 'shown'

        # Show or hide element
        @dropdown.toggleClass "shown"
        @element.parent().toggleClass 'active'

class OffcanvasTouch
    #   Public: Constructor for offcanvas
    #
    #   @element - Element that toggles the offcanvas
    #   @location - Location of offcanvas (Left/Right)
    #   @offcanvas - Offcanvas class ref
    constructor: (@element, @location, @offcanvas) ->
        @endThreshold = 130
        @startThreshold = if @element.hasClass 'navbar-offcanvas-right' then $("body").outerWidth() - 60 else 20
        @maxStartThreshold = if @element.hasClass 'navbar-offcanvas-right' then $("body").outerWidth() - 20 else 60
        @currentX = 0

        # Add touch start event
        $(document).on "touchstart", @_touchStart

        # Add touch move event
        $(document).on "touchmove", @_touchMove

        # Add touch end event
        $(document).on "touchend", @_touchEnd

    #   Private: Touch start
    #
    #   e - Event target
    _touchStart: (e) =>
        @startX = e.originalEvent.touches[0].pageX

    #   Private: Touch move
    #
    #   e - Event target
    _touchMove: (e) =>
        return true if $(e.target).parents('.navbar-offcanvas').length > 0

        if @startX > @startThreshold and @startX < @maxStartThreshold
            e.preventDefault()

            x = e.originalEvent.touches[0].pageX - @startX
            x = if @element.hasClass 'navbar-offcanvas-right' then -x else x

            if Math.abs(x) < @element.outerWidth()
                # Get CSS to move element
                @element.css @_getCss x
        else if @element.hasClass 'in'
            e.preventDefault()

            x = e.originalEvent.touches[0].pageX + (@currentX - @startX)
            x = if @element.hasClass 'navbar-offcanvas-right' then -x else x

            if Math.abs(x) < @element.outerWidth()
                # Get CSS to move element
                @element.css @_getCss x

    #   Private: Touch end
    #
    #   e - Event target
    _touchEnd: (e) =>
        return true if $(e.target).parents('.navbar-offcanvas').length > 0

        x = e.originalEvent.changedTouches[0].pageX
        end = if @element.hasClass 'navbar-offcanvas-right' then Math.abs(x) > (@endThreshold + 50) else x < (@endThreshold + 50)

        if @element.hasClass('in') and end
            @currentX = 0

            # Show or hide the element
            @element.removeClass 'in'
                .css @_clearCss()
        else if Math.abs(x - @startX) > @endThreshold and @startX > @startThreshold and @startX < @maxStartThreshold
            @currentX = if @element.hasClass 'navbar-offcanvas-right' then -@element.outerWidth() else @element.outerWidth()

            # Show or hide the element
            @element.toggleClass 'in'
                .css @_clearCss()
        else
            @element.css @_clearCss()

        # Overflow on body element
        @offcanvas.bodyOverflow()

    #   Private: Get CSS
    #
    #   x - Location of touch
    _getCss: (x) =>
        x = if @element.hasClass 'navbar-offcanvas-right' then -x else x

        {
            "-webkit-transform": "translate3d(#{x}px, 0px, 0px)"
            "-webkit-transition-duration": "0s"
            "-moz-transform": "translate3d(#{x}px, 0px, 0px)"
            "-moz-transition": "0s"
            "-o-transform": "translate3d(#{x}px, 0px, 0px)"
            "-o-transition": "0s"
            "transform": "translate3d(#{x}px, 0px, 0px)"
            "transition": "0s"
        }

    #   Private: Clear CSS properties
    _clearCss: =>
        {
            "-webkit-transform": ""
            "-webkit-transition-duration": ""
            "-moz-transform": ""
            "-moz-transition": ""
            "-o-transform": ""
            "-o-transition": ""
            "transform": ""
            "transition": ""
        }

class Offcanvas
    #   Public: Constructor for offcanvas
    #
    #   @element - Element that toggles the offcanvas
    constructor: (@element) ->
        # Does this element have a target
        target = if @element.attr 'data-target' then @element.attr 'data-target' else false

        # Continue if target is not false
        if target
            # Get target element
            @target = $(target)

            # Target must be available before running
            if @target.length
                # Get the location of the offcanvas menu
                @location = if @target.hasClass "navbar-offcanvas-right" then "right" else "left"

                @target.addClass if transform then "offcanvas-transform" else "offcanvas-position"

                # Click event on element
                @element.on "click", @_clicked

                # Click event on document
                $(document).on "click", @_documentClicked

                # Should touch be added to this target
                if @target.hasClass 'navbar-offcanvas-touch'
                    touch = true

                    # Create touch class
                    t = new OffcanvasTouch @target, @location, @

                # Get all dropdown menu links and create a class for them
                @target.find(".dropdown-toggle").each ->
                    d = new OffcanvasDropdown @
            else
                # Log a warning
                console.warn "Offcanvas: Can't find target element with selector #{target}."
        else
            # Just log a warning
            console.warn 'Offcanvas: `data-target` attribute must be present.'

    #   Private: Clicked element
    #
    #   e - Event data
    _clicked: (e) =>
        e.preventDefault()

        @_sendEventsBefore()

        # Hide all other off canvas menus
        $(".navbar-offcanvas").removeClass 'in'

        # Toggle in class
        @target.toggleClass 'in'
        @bodyOverflow()

    #   Private: Document click event to hide offcanvas
    #
    #   e - Event data
    _documentClicked: (e) =>
        # Get clicked element
        clickedEl = $(e.target)

        if !clickedEl.hasClass('offcanvas-toggle') and clickedEl.parents('.offcanvas-toggle').length is 0 and clickedEl.parents('.navbar-offcanvas').length is 0 and !clickedEl.hasClass('navbar-offcanvas')
            if @target.hasClass 'in'
                e.preventDefault()

                @_sendEventsBefore()

                @target.removeClass 'in'
                @bodyOverflow()

    #   Private: Send before events
    _sendEventsBefore: =>
        # Send events
        if @target.hasClass 'in'
            @target.trigger 'show.bs.offcanvas'
        else
            @target.trigger 'hide.bs.offcanvas'

    #   Private: Send after events
    _sendEventsAfter: =>
        # Send events
        if @target.hasClass 'in'
            @target.trigger 'shown.bs.offcanvas'
        else
            @target.trigger 'hidden.bs.offcanvas'

    #   Public: Overflow on body
    bodyOverflow: =>
        @_sendEventsAfter()

        $("body").css
            overflow: if @target.hasClass 'in' then 'hidden' else ''


#   Transform checker
#
#   Checks if transform3d is available for us to use
transformCheck = =>
    el = document.createElement 'div'
    translate3D = "translate3d(0px, 0px, 0px)"
    regex = /translate3d\(0px, 0px, 0px\)/g

    el.style.cssText = "-webkit-transform: #{translate3D}; -moz-transform: #{translate3D}; -o-transform: #{translate3D}; transform: #{translate3D}"
    asSupport = el.style.cssText.match regex

    @transform = asSupport.length?

$ ->
    # Work out if transform3d is available for use
    transformCheck()

    $('[data-toggle="offcanvas"]').each ->
        oc = new Offcanvas $(this)
