#!/usr/bin/perl
use v5.14;
use Time::Moment;

my $file_name = '/root/learning/perl/ip_stastic.txt';
my $log_file_name = '/root/learning/perl/ip_stastic_log.txt';

system 'touch', $file_name unless -e $file_name;
system 'touch', $log_file_name unless -e $log_file_name;
open (my $fh, '<', $file_name)
	or die "can't open file: $!";
chomp(my $ip_now = `curl icanhazip.com`);
my %ips;
while(<$fh>) {
	chomp;
	my($ip, $count) = split;
	$ips{$ip} = $count;
}

my $flag_ip = 0;	#ip in keys or not
my $flag_ex = 0; #ip change or not
my @keys = keys %ips;
for (@keys){
	$flag_ip = 1 if $ip_now eq $_;
	$flag_ex = 1 if $_ == -1 && $ips{$_} ne $ip_now;
}
if($flag_ip == 1 && $flag_ex == 1){
	for (sort keys %ips){
		if($_ eq $ip_now){
			$ips{$_} += 1;
		}
		if($ips{$_} == -1){
			delete $ips{$_};
		}
	}
	$ips{-1} = $ip_now;
}

if($flag_ip == 0 && $flag_ex == 1){
	for (sort keys %ips){
		if($ips{$_} == -1){
			delete $ips{$_};
		}
	}
	$ips{-1} = $ip_now;
	$ips{$ip_now} = 1;
}

if($flag_ip == 0 && $flag_ex ==0){
	$ips{-1} = $ip_now;
	$ips{$ip_now} = 1;
}

close $fh;

open ($fh, '>', $file_name)
	or die "can't open file: $!";
for (sort keys %ips){
	print $fh "$_ $ips{$_}\n";
}
close $fh;
open ($fh, '>>', $log_file_name);
my $tm = Time::Moment->now;
print $fh "complete time is $tm\n";
close $fh;
