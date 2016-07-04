Bootloader Grub2
================
http://www.gnu.org/software/grub/manual/grub.html
http://www.gnu.org/software/grub/grub-documentation.html


Runtime Tools
-------------
grub-mkconfig:
    make the template of the grub.cfg file

grub-reboot <idx>:
    save current entry index to 'prev_saved_entry',
    and save <idx> to 'saved_entry' in grubenv.

grub-editenv [grubenv-file] <command> <var-name>:
    Set/Delete/List the variables in grubenv.

grub-menulst2cfg:
    Convert the grub 0.97 conf file to grub2 cfg file.
