for file in *.mp4; do
    withoutSuffix="$(basename "$file" .mp4)"
    echo $withoutSuffix
    ./ffmpeg -i $file -c copy -an $withoutSuffix"new.mp4"
    rm $file
    mv $withoutSuffix"new.mp4" $file
done