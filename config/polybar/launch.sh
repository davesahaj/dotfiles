
killall -q polybar

polybar example 2>&1 | tee -a /tmp/polybar1.log & disown

echo "Bars launched..."
